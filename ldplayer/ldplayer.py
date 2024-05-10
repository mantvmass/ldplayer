import subprocess


class LDPlayer:
    
    
    __ldconsole: str


    def __init__(self, ldconsole):
        self.__ldconsole = ldconsole
        
        
    def instances(self) -> list:
        process = subprocess.Popen([self.__ldconsole, "list"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = process.communicate()
        output = output.decode("utf-8")
        return [ins for ins in output.split("\r\n") if ins != '']
    
    
    def create(self, instance_name: str) -> bool:
        process = subprocess.Popen([self.__ldconsole, "add", "--name", instance_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        return process.returncode == len(self.instances()) - 1


    def modify_emulator(self, instance_name: str) -> bool:
        process = subprocess.Popen(
            [
                self.__ldconsole, "modify", "--name", instance_name, "--resolution", "950,540,240",
                "--cpu", "2", "--memory", "2048", "--autorotate", "0", "--lockwindow", "1", "--root", "1"
            ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        process.communicate()
        return process.returncode == 0


    def install_app(self, name: str, filename: str) -> bool:
        """
        Installs an app on the ldplayer emulator.
        
        :param name: The name or index of the VM instance to install the app on.
        :param filename: The path to the APK file to install.
        :return: True if the installation was successful, False otherwise.
        """
        command = [self.__ldconsole, "installapp", "--name", name, "--filename", filename]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        return process.returncode == 0
    
    
    def launch(self, instance: str) -> bool:
        command = [self.__ldconsole, "launch"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        return process.returncode == 0
    
    
    def copy(self, instance_name: str, source: str) -> bool:
        before = len(self.instances())
        subprocess.Popen([self.__ldconsole, "copy", "--name", instance_name, "--from", str(source)])
        after = len(self.instances())
        return (before + 1) == after
    
    
    def remove(self, instance: str) -> bool:
        command = [self.__ldconsole, "remove"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        return process.returncode == 0
    
    
    def quit(self, instance: str) -> bool:
        command = [self.__ldconsole, "quit"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        return process.returncode == 0
    
    
    def quitAll(self):
        subprocess.Popen([self.__ldconsole, "quitall"])
        
    
    def reboot(self, instance: str) -> bool:
        command = [self.__ldconsole, "reboot"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        return process.returncode == 0
    
    
    def running_lists(self):
        process = subprocess.Popen([self.__ldconsole, "runninglist"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = process.communicate()
        output = output.decode("utf-8")
        return [ins for ins in output.split("\r\n") if ins != '']
    
    
    def is_running(self, instance: str) -> bool:
        command = [self.__ldconsole, "isrunning"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = process.communicate()
        return output.decode("utf-8") == "running"