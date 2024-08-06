:: assuming that new_folder mentioned is from the file_cd.bat
:: https://www.ionos.com/digitalguide/server/tools/batch-commands/
:: https://www.instructables.com/Batch-Scripting-Using-If-Statements-for-Decision-M/

if exist "new_folder" (
	cd new_folder
	mkdir if_folder
	echo if_folder was created!
) else (
	echo Folder "new_folder" not found try running file_cd.bat first
)

if exist "if_folder" (
	cd if_folder
	mkdir hyperionDev
	echo Folder hyperionDev was created!
) else (
	mkdir new-projects
	echo Folder new-projects was created!
)
cmd.exe
