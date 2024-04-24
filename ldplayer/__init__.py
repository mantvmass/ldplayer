import subprocess
import configparser
import tkinter as tk
import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a file handler which logs even debug messages
fh = logging.FileHandler('ldplayer.log')
fh.setLevel(logging.DEBUG)

# Create a console handler which logs even debug messages
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create a formatter and set the formatter for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)



class LDPlayer:
    __ldconsole: str

    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file, encoding='ISO-8859-1')
        self.__ldconsole = self.config.get('LDPlayer', 'ldconsole')
        logger.debug(f"LDPlayer initialized with ldconsole: {self.__ldconsole}")

    def instances(self) -> list:
        logger.debug("Getting instances")
        process = subprocess.Popen([self.__ldconsole, "list"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        output, err = process.communicate()
        output = output.decode("utf-8")
        logger.debug(f"Instances: {output}")
        return [ins for ins in output.split("\r\n") if ins != '']

    def create(self, instance_name: str) -> bool:
        logger.debug(f"Creating instance: {instance_name}")
        process = subprocess.Popen([self.__ldconsole, "add", "--name", instance_name], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        logger.debug(f"Instance created: {instance_name}")
        return process.returncode == len(self.instances()) - 1

    def modify_emulator(self, instance_name: str) -> bool:
        logger.debug(f"Modifying emulator: {instance_name}")
        process = subprocess.Popen([self.__ldconsole, "modify", "--name", instance_name, "--resolution", "950,540,240",
                                    "--cpu", "2", "--memory", "2048", "--autorotate", "0", "--lockwindow", "1",
                                    "--root", "1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        process.communicate()
        logger.debug(f"Emulator modified: {instance_name}")
        return process.returncode == 0

    def install_app(self, name: str, filename: str) -> bool:
        """
        Installs an app on the LDPlayer emulator.
        :param name: The name or index of the VM instance to install the app on.
        :param filename: The path to the APK file to install.
        :return: True if the installation was successful, False otherwise.
        """
        logger.debug(f"Installing app: {filename} on instance: {name}")
        command = [self.__ldconsole, "installapp", "--name", name, "--filename", filename]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        logger.debug(f"App installed: {filename} on instance: {name}")
        return process.returncode == 0

    def launch(self, instance: str) -> bool:
        logger.debug(f"Launching instance: {instance}")
        command = [self.__ldconsole, "launch"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        logger.debug(f"Instance launched: {instance}")
        return process.returncode == 0

    def copy(self, instance_name: str, source: str) -> bool:
        logger.debug(f"Copying instance: {instance_name} from: {source}")
        before = len(self.instances())
        subprocess.Popen([self.__ldconsole, "copy", "--name", instance_name, "--from", str(source)])
        after = len(self.instances())
        logger.debug(f"Instance copied: {instance_name} from: {source}")
        return (before + 1) == after

    def remove(self, instance: str) -> bool:
        logger.debug(f"Removing instance: {instance}")
        command = [self.__ldconsole, "remove"]
        if str(instance).isnumeric():
            command.extend(["--index", str(instance)])
        else:
            command.extend(["--name", instance])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        logger