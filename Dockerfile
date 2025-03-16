FROM artemisfowl004/vid-compress
WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
  && apt-get install libgl1 -y \
  && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 \
  && apt-get install wget -y \
  && apt-get install xz-utils -y \
  && wget -O ffmpeg.tar.xz "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz" \
  && tar -xvf ffmpeg.tar.xz \
  && cp ffmpeg-master-latest-linux64-gpl/bin/* /usr/bin \
  && rm -rf ffmpeg.tar.xz ffmpeg-master-latest-linux64-gpl \
  && pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash", "start.sh"]
