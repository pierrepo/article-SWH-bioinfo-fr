# Transcription d'une vidéo YouTube

30/12/2024

## Ressources

Vidéo source : [Tuto@Mate#64 Pierre Poulain présente Git et l'archive Software Heritage](https://www.youtube.com/watch?v=GjVrZbU0PB0)

L'[API Whisper de Groq](https://console.groq.com/docs/speech-text) supporte des fichiers audio au format mp3, mp4, wav... avec une taille maximale de 25 Mo.

Les modèles supportant le français sont `whisper-large-v3-turbo` et `whisper-large-v3`. Le dernier est un peu plus lent, mais fait aussi moins d'erreurs.

Groq recommande également de réduire la qualité du fichier à du mono en 16 000 Hz :

```bash
ffmpeg \
  -i <your file> \
  -ar 16000 \
  -ac 1 \
  -map 0:a: \
  <output file name>
```

## Préparation du fichier audio

Installer [Pixi](https://pixi.sh/) si besoin.

Télécharger le fichier audio de la vidéo :

```bash
pixi run yt-dlp -f 140 -o audio_full.m4a https://www.youtube.com/watch?v=GjVrZbU0PB0
```

Découper la partie intéressante, de 1:32:50 à 1:52:45 :

```bash
pixi run ffmpeg \
  -i audio_full.m4a \
  -ss 01:32:50 -to 01:52:45 \
  -c:a libmp3lame \
  audio.mp3
```

Passer en mono 16 000 Hz :

```bash
pixi run ffmpeg \
  -i audio.mp3 \
  -ar 16000 \
  -ac 1 \
  -map 0:a: \
  audio_clean.mp3
```

Vérifier que le fichier audio final a une taille inférieure à 25 Mo :

```bash
$ ls -lh audio*
-rw-rw-r-- 1 pierre pierre 3,5M déc.  30 11:34 audio_clean.mp3
-rw-rw-r-- 1 pierre pierre 122M oct.  11 17:03 audio_full.m4a
-rw-rw-r-- 1 pierre pierre  19M déc.  30 11:33 audio.mp3
```

## Transcription

Exporter la [clé d'API Groq](https://console.groq.com/keys) :

```bash
export GROQ_API_KEY=gsk_...
```

Lancer la transcription :

```bash
pixi run python transcript.py > audio_text.txt
```

## Préparation de l'article de blog

Prompt ChatGPT 4o :

> Organise le texte suivant sur Software Heritage sous la forme d'un article de blog à destination de bioinformaticiens. L'article doit être structuré et factuel. N'enjolive pas mais donne envie aux lecteurs d'archiver leur code dans Software Heritage :
> [contenu de audio_text.txt]

[Réponse](2024-12-30_chatgpt_text.md)