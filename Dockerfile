FROM python:3
# Change base to new ubuntu

RUN apt-get update && apt-get install -y \
    rtl-sdr \
    librtlsdr-dev \
    gnuradio \
    gnuradio-dev

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt
     
ENV PYTHONPATH "${PYTHONPATH}:/usr/lib/python3/dist-packages"

COPY app /app/
ENTRYPOINT ["python3", "/app/app.py"]
