#  AWS Cloud Automation & CI/CD Pipeline

##  O projekcie
Projekt to w pełni zautomatyzowane, chmurowe środowisko wdrożeniowe zbudowane od zera, pozwalające na hostowanie aplikacji webowej. 
Zamiast ręcznego wyklikiwania serwerów i kopiowania plików, cały cykl życia infrastruktury i aplikacji jest zarządzany przez kod (Infrastructure as Code) oraz CI/CD.

##  Architektura i Przepływ Pracy
Projekt łączy cztery niezależne warstwy w jeden spójny system:

1. **Provisioning (Terraform):** Kod definiujący architekturę w chmurze AWS. Powołuje do życia maszynę wirtualną (EC2 t3.micro) oraz konfiguruje reguły sieciowe (Security Groups otwierające porty HTTP i SSH).
2. **Konfiguracja (Ansible):** Playbooki, które automatycznie instalują środowisko Docker na surowym systemie Ubuntu oraz konfigurują Nginx jako Reverse Proxy, oddzielając ruch sieciowy od samej aplikacji.
3. **Aplikacja (Docker):** Aplikacja "To-Do" napisana w języku Python (Flask), spakowana w lekki, izolowany kontener.
4. **Automatyzacja (GitHub Actions):** Dwustopniowy pipeline chroniący produkcję:
   - **CI (Continuous Integration):** Uruchamia testy jednostkowe (`pytest`). Chroni serwer przed wdrożeniem zepsutego kodu.
   - **CD (Continuous Deployment):** Po zdanych testach buduje nowy obraz, wysyła go na Docker Hub i aktualizuje kontener na serwerze AWS przez protokół SSH.

##  Wykorzystane Technologie
- **Chmura:** AWS (EC2, VPC, Security Groups)
- **IaC:** Terraform
- **Zarządzanie konfiguracją:** Ansible
- **Konteneryzacja:** Docker, Docker Hub
- **CI/CD:** GitHub Actions
- **Język / Framework:** Python 3.11, Flask, Pytest

##  Główne wyzwania i to, czego dowodzi ten projekt
Podczas budowy tego projektu rozwiązałem kilka klasycznych problemów inżynieryjnych:
* **Idempotentność infrastruktury:** Playbooki Ansible i kod Terraform są napisane tak, aby można było je uruchamiać wielokrotnie bez niszczenia działającego systemu.
* **Bezpieczeństwo połączeń:** GitHub Actions autoryzuje się na serwerze AWS używając wyłącznie prywatnych kluczy asymetrycznych, a sam serwer nie wystawia na zewnątrz żadnych niepotrzebnych portów.
* **Ochrona produkcji (Fail-Fast):** Wdrożenie mechanizmu powiązań (`needs`) w GitHub Actions sprawia, że błąd w testach natychmiast przerywa cały pipeline, chroniąc działającą wersję aplikacji przed awarią.