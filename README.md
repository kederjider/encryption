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

<pre><code> sudo apt update && sudo apt upgrade -y </code></pre>
<pre><code> sudo apt install -y git openssh-client python3 python3-pip python3-venv </code></pre>

Cek versi:

<pre><code> python3 --version </code></pre>
<pre><code> git --version </code></pre>
<pre><code> ssh -V </code></pre>

## 2) Membuat SSH Key GitHub

Buat SSH key baru (disarankan ed25519):

<pre><code> ssh-keygen -t ed25519 -C "email-kamu@domain.com" </code></pre>

Saat muncul lokasi file, tekan Enter untuk default:
/home/username/.ssh/id_ed25519

Aktifkan ssh-agent dan tambahkan key:

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

Tampilkan public key:

<pre><code>cat ~/.ssh/id_ed25519.pub </code></pre>

Copy seluruh output key, lalu buka GitHub:

- Settings
- SSH and GPG keys
- New SSH key
- Paste key lalu Save

## 3) Tes Koneksi SSH ke GitHub

<pre><code>ssh -T git@github.com </code></pre>

Jika berhasil biasanya muncul pesan sambutan dari GitHub.

## 4) Clone Repository via SSH

Contoh format clone:

git clone git@github.com:USERNAME/NAMA-REPO.git

Masuk ke folder project:

cd NAMA-REPO

Jika project sudah ada di server dan Anda hanya ingin update:

<pre><code>git pull origin main</code></pre>

## 5) Membuat Virtual Environment Python

Di root project, jalankan:

<pre><code>python3 -m venv venv</code></pre>
source venv/bin/activate

Setelah aktif, prompt terminal biasanya menampilkan (venv).

Upgrade pip:

<pre><code>pip install --upgrade pip</code></pre>

## 6) Install Library dari req.txt

Install dependency:

<pre><code>pip install -r req.txt</code></pre>

Jika ada error encoding pada req.txt, konversi dulu ke UTF-8:

<pre><code>iconv -f UTF-16 -t UTF-8 req.txt -o req.txt</code></pre>
<pre><code>pip install -r req.txt</code></pre>

## 7) Membuat File .env

Aplikasi ini memakai variabel berikut:

- BOT_TOKEN
- CHAT_ID

Buat file .env di root project:

<pre><code>nano .env</code></pre>

Isi dengan contoh berikut:

BOT_TOKEN=isi_token_bot_telegram_kamu
CHAT_ID=isi_chat_id_telegram_kamu

Simpan file dan keluar dari editor.

## 8) Cara pakai

**🔐 Encrypt file**

<pre><code>python3 encrypt_file.py enc file.txt file.enc password123</code></pre>

**🔓 Decrypt file**

<pre><code>python3 encrypt_file.py dec file.enc file.txt password123</code></pre>

**📁 Contoh real (backup VPS kamu)**

<pre><code>tar -czf backup.tar.gz /var/www
<pre><code>python encrypt_file.py enc backup.tar.gz backup.enc mypassword</code></pre>

**☁️ Upload ke Google Drive**

☁️ Upload ke Google Drive

## 9) Update Kode dari GitHub

Jika sudah pernah clone:

cd NAMA-REPO
<pre><code>source venv/bin/activate</code></pre>
<pre><code>git pull origin main</code></pre>
<pre><code>pip install -r req.txt</code></pre>

Selesai. Jika butuh, Anda bisa lanjut setup systemd + Nginx agar aplikasi auto-start dan berjalan stabil setelah reboot.
