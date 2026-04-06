# Panduan Enc Dan Dnc Untuk Menjalankan DiUbuntu

Dokumen ini menjelaskan langkah dari nol:

1. Membuat SSH key
2. Menambahkan SSH key ke GitHub
3. Clone repository via SSH
4. Install Python di Ubuntu
5. Membuat virtual environment
6. Install library dari req.txt
7. Membuat file .env
8. Cara pakai
9. Update Kode dari GitHub

## 1) Persiapan di Ubuntu

Jalankan perintah berikut:

sudo apt update
sudo apt install -y git openssh-client python3 python3-pip python3-venv

Cek versi:

python3 --version
git --version
ssh -V

## 2) Membuat SSH Key GitHub

Buat SSH key baru (disarankan ed25519):

ssh-keygen -t ed25519 -C "email-kamu@domain.com"

Saat muncul lokasi file, tekan Enter untuk default:
/home/username/.ssh/id_ed25519

Aktifkan ssh-agent dan tambahkan key:

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

Tampilkan public key:

cat ~/.ssh/id_ed25519.pub

Copy seluruh output key, lalu buka GitHub:

- Settings
- SSH and GPG keys
- New SSH key
- Paste key lalu Save

## 3) Tes Koneksi SSH ke GitHub

ssh -T git@github.com

Jika berhasil biasanya muncul pesan sambutan dari GitHub.

## 4) Clone Repository via SSH

Contoh format clone:

git clone git@github.com:USERNAME/NAMA-REPO.git

Masuk ke folder project:

cd NAMA-REPO

Jika project sudah ada di server dan Anda hanya ingin update:

git pull origin main

## 5) Membuat Virtual Environment Python

Di root project, jalankan:

python3 -m venv venv
source venv/bin/activate

Setelah aktif, prompt terminal biasanya menampilkan (venv).

Upgrade pip:

pip install --upgrade pip

## 6) Install Library dari req.txt

Install dependency:

pip install -r req.txt

Jika ada error encoding pada req.txt, konversi dulu ke UTF-8:

iconv -f UTF-16 -t UTF-8 req.txt -o req.txt
pip install -r req.txt

## 7) Membuat File .env

Aplikasi ini memakai variabel berikut:

- BOT_TOKEN
- CHAT_ID

Buat file .env di root project:

nano .env

Isi dengan contoh berikut:

BOT_TOKEN=isi_token_bot_telegram_kamu
CHAT_ID=isi_chat_id_telegram_kamu

Simpan file dan keluar dari editor.

## 8) Cara pakai

**🔐 Encrypt file**

python3 encrypt_file.py enc file.txt file.enc password123

**🔓 Decrypt file**

python3 encrypt_file.py dec file.enc file.txt password123

**📁 Contoh real (backup VPS kamu)**

tar -czf backup.tar.gz /var/www
python encrypt_file.py enc backup.tar.gz backup.enc mypassword

**☁️ Upload ke Google Drive**

☁️ Upload ke Google Drive

## 9) Update Kode dari GitHub

Jika sudah pernah clone:

cd NAMA-REPO
source venv/bin/activate
git pull origin main
pip install -r req.txt

Selesai. Jika butuh, Anda bisa lanjut setup systemd + Nginx agar aplikasi auto-start dan berjalan stabil setelah reboot.
