# récupération de l'image de départ
FROM ubuntu:latest

# Installation de pip
RUN apt update && apt install -y python3-pip
# Copie des fichiers vers le container
ADD ./inferenceEngine/requirements.txt /tmp/requirements.txt

# installation des dépendances Python
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Copy de notre code
ADD ./inferenceEngine /opt/inferenceEngine/
WORKDIR /opt/inferenceEngine

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
# RUN adduser -D myuser
# USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 

