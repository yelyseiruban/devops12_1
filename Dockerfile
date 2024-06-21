# Użyj oficjalnego obrazu Jenkinsa jako bazowego obrazu
FROM jenkins/jenkins:lts

# Użytkownik root jest wymagany do instalacji pakietów
USER root

# Aktualizacja pakietów systemowych i instalacja Pythona oraz pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Ustawienie ścieżki PATH - dodanie Pythona do ścieżki
ENV PATH="/usr/bin/python3:${PATH}"

# Przełączenie z powrotem do użytkownika jenkins
USER jenkins
