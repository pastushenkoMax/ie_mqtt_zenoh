FROM python:3.10
WORKDIR /mqtt_zenoh_v2/src/app
COPY . .
RUN pip install eclipse-zenoh
CMD ["python", "z_pub.py"]
