FROM python:3

ADD detection.py .
ADD epy_block_1_0_0_0.py .
ADD epy_block_0_2_0_0_0.py .
ADD event.py .

RUN apt-get update && apt-get install -y \
    rtl-sdr \
    librtlsdr-dev \
    gnuradio \
    gnuradio-dev
     
RUN mkdir /lightning
RUN mkdir /lightning/data
     
ENV PYTHONPATH "${PYTHONPATH}:/usr/lib/python3/dist-packages"

CMD ["python3", "./detection.py"]
