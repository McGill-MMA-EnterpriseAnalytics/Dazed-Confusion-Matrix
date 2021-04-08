# Set Python version
FROM python:3.7
# Copy entire project
COPY . /app
WORKDIR /app
# Install requirements
RUN pip3 install -r requirements.txt
# Test application
RUN pytest
# Clear port to run app
EXPOSE 80
# RUN mkdir ~/.streamlit
# RUN cp config.toml ~/.streamlit/config.toml
# RUN cp credentials.toml ~/.streamlit/credentials.toml
# Go into the dashboard folder
WORKDIR /app/App
# Run app
ENTRYPOINT ["streamlit", "run", "app.py"]
