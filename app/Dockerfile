FROM python:3.11-slim

# 2. Ustaw folder roboczy wewnątrz kontenera
WORKDIR /app

# 3. Skopiuj plik z zależnościami
COPY requirements.txt .

# 4. Zainstaluj biblioteki
RUN pip install --no-cache-dir -r requirements.txt

# 5. Skopiuj resztę kodu aplikacji
COPY . .

# 6. Poinformuj, że aplikacja działa na porcie 8080
EXPOSE 8080

# 7. Komenda, która uruchomi aplikację po starcie kontenera
CMD ["python", "app.py"]