import subprocess
import re
import pandas as pd

def get_file_sizes(directory_url, cert_path, ca_path):
    try:
        # Esegui il comando davix-ls per ottenere la lista dei file e le loro dimensioni
        result = subprocess.run([
            'davix-ls', '-l', '-E', cert_path, '--capath', ca_path, directory_url
        ], capture_output=True, text=True, check=True)
        
        # Leggi l'output del comando
        output = result.stdout
        
        # Dichiara un dizionario per contenere i nomi dei file e le loro dimensioni
        file_sizes = {}
        
        # Analizza l'output riga per riga
        for line in output.splitlines():
            # Ignora le righe non relative ai file (come intestazioni o directory)
            if line.endswith('.root') and line:
                parts = line.split()
                # L'ultima parte è il nome del file
                file_name = parts[-1]
                # La quarta parte è la dimensione del file
                file_size = parts[2]
                file_sizes[file_name] = int(file_size)
        
        return file_sizes
    
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'esecuzione di davix-ls: {e}")
        return {}

def find_folder(username, remote_dir, dataset_label, cert_path, ca_path):
    results = subprocess.run([
        'davix-ls', '-E', cert_path, '--capath', ca_path, "davs://stwebdav.pi.infn.it:8443/cms/store/user/"+username+"/"+remote_dir+"/"+dataset_label+"/"
    ], capture_output=True, text=True, check=True)
    subfold = results.stdout.splitlines()
    subfold.sort()
    subfold = subfold[-1]

    return "davs://stwebdav.pi.infn.it:8443/cms/store/user/"+username+"/"+remote_dir+"/"+dataset_label+"/"+subfold

def job_exit_code(job_logFile):
    exit_code = None

    with open(job_logFile, "r") as f:
        lines = f.readlines()

    # Search for the last line with "Normal termination"
    for line in reversed(lines):
        match = re.search(r'return value (\d+)\)', line)
        if match:
            exit_code = int(match.group(1))
            break

    # if exit_code is not None:
    #     print(f"Exit code: {exit_code}")
    # else:
    #     print("No exit code found.")

    return exit_code

def checkSubmitStatus(username, uid, sample, running_folder, remote_folder_name):
    import os
    # print("Sample: ", sample.label)
    listoffile = os.listdir(running_folder+"/"+sample.label)

    # check number of total number of files that should have been created
    jobs_total = 0 
    for f in listoffile: 
        if f.startswith("file"):
            n = int(f.split("file")[-1])
            if n>jobs_total: jobs_total = n
    jobs_total += 1


    # check number of files that have been actually created
    davixfolder                     = find_folder(username, remote_folder_name, sample.label, "/tmp/x509up_u"+str(uid), "/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/")
    # print("davixfolder: ", davixfolder)
    file_sizes                      = get_file_sizes(davixfolder, "/tmp/x509up_u"+str(uid), "/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/")
    total_files_onTier              = len(file_sizes)
    fileNumbers_onTier              = [int(file_name.split("_")[-1].split(".")[0]) for file_name, file_size in file_sizes.items()]
    njobs_toResubmit     = 0
    njobs_notFoundOnTier = 0
    njobs_emptyFile      = 0
    jobs_toResubmit_notFoundOnTier = []
    jobs_toResubmit_emptyFile      = []
    for jobNumber in range(jobs_total):
        resubmit_job     = False
        file_name        = f"tree_hadd_{jobNumber}.root"
        if jobNumber not in fileNumbers_onTier:
            # print(f"Job {jobNumber} not found on tier")
            njobs_notFoundOnTier            += 1
            njobs_toResubmit                += 1
            jobs_toResubmit_notFoundOnTier.append(jobNumber)
            resubmit_job                     = True
        else:
            file_size = file_sizes[file_name]
            if file_size < 1000:
                # print(f"File: {file_name}, Size: {file_size} bytes")
                njobs_emptyFile             += 1
                njobs_toResubmit            += 1
                jobs_toResubmit_emptyFile.append(jobNumber)
                resubmit_job                 = True

        if resubmit_job:
            file_num            = str(jobNumber)
            sample_folder       = running_folder+"/"+sample.label+"/file"+file_num+"/"
            # print("Removing empty file from tier...  "+file_name)
            # print("davix-rm "+davixfolder+"/"+file_name+" -E /tmp/x509up_u"+str(uid)+" --capath /cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/")
            # os.popen("davix-rm "+davixfolder+"/"+file_name+" -E /tmp/x509up_u"+str(uid)+" --capath /cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/")
            # print("Resubmitting...")
            # print("condor_submit "+sample_folder+"condor.sub")
            # os.popen("condor_submit "+sample_folder+"/condor.sub")
            # print("\n")

    return jobs_total, total_files_onTier, njobs_toResubmit, njobs_notFoundOnTier, njobs_emptyFile, jobs_toResubmit_notFoundOnTier, jobs_toResubmit_emptyFile


def summarize_job_status(username, uid, samples, running_folder, remote_folder_name):
    summary = []

    for sample in samples:
        try:
            jobs_total, total_on_tier, to_resubmit, not_found, empty, jobs_toResubmit_notFoundOnTier, jobs_toResubmit_emptyFile = checkSubmitStatus(username, uid, sample, running_folder, remote_folder_name)
            summary.append({
                "Sample": sample.label,
                "Jobs Total": jobs_total,
                "Files on Tier": total_on_tier,
                "To Resubmit": to_resubmit,
                "Not Found on Tier": not_found,
                "Empty Files": empty,
                "Jobs Not Found": jobs_toResubmit_notFoundOnTier,
                "Jobs Empty": jobs_toResubmit_emptyFile,
            })
        except Exception as e:
            summary.append({
                "Sample": sample.label,
                "Jobs Total": "ERROR",
                "Files on Tier": "ERROR",
                "To Resubmit": "ERROR",
                "Not Found on Tier": "ERROR",
                "Empty Files": "ERROR",
                "Jobs Not Found": "ERROR",
                "Jobs Empty": "ERROR",
            })
            print(f"Error processing sample {sample.label}: {e}")

    df = pd.DataFrame(summary)
    return df









# # Esempio di utilizzo
# folder = find_folder("Run3Analysis_Tprime", "TprimeToTZ_1800_2022", "/tmp/x509up_u140541", "/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/")
# # directory_url = "davs://stwebdav.pi.infn.it:8443/cms/store/user/acagnott/Run3Analysis_Tprime/DataEGammaC_2022/20240703_092359/"
# # cert_path = "/tmp/x509up_u140541"
# # ca_path = "/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/"
# file_sizes = get_file_sizes(folder, "/tmp/x509up_u140541", "/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/")
# for file_name, file_size in file_sizes.items():
#     if file_size <1000:
#         print(f"File: {file_name}, Size: {file_size} bytes")