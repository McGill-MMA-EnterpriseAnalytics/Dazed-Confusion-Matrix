FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 80
# RUN mkdir ~/.streamlit
# RUN cp config.toml ~/.streamlit/config.toml
# RUN cp credentials.toml ~/.streamlit/credentials.toml
WORKDIR /app/App
# CMD -o logLevel=ERROR -L 80:$IP_ADDRESS:80 $USERNAME@$IP_ADDRESS
# CMD redir --laddr=0.0.0.0 --lport=80 --caddr=0.0.0.0 --cport=80
ENTRYPOINT ["streamlit", "run", "app.py"]
# CMD ["app.py"]
