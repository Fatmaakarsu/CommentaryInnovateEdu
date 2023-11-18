
## Proje yükleme adımları

Öncelikle GitHub reposundan (https://github.com/Fatmaakarsu/CommentaryInnovateEdu.git) projeyi klonlayarak başlayalım. 
```sh
git clone https://github.com/Fatmaakarsu/CommentaryInnovateEdu.git
```
Sistemdeki paket listesini güncelleyelim.
```sh
apt-get update
```
#### Projenin çalışması için gerekli kurulumları yapalım:

Python 3 için paket yöneticisi olan pip'in kurulumunu sağlayalım.

```sh
apt-get install python3-pip
```
Projede kullanılan Flask web uygulama frameworkunu yükleyelim.

```sh
pip install flask
```

Flask uygulamalarında SQL veritabanları ile etkileşimde bulunmak için kullanılan Flask-SQLAlchemy kütüphanesini yükleyelim.

```sh
pip install flask_sqlalchemy
```
Flask uygulamalarında şifreleme ve hashleme işlemleri için kullanılan Flask-Bcrypt kütüphanesini yükleyelim.

```sh
pip install flask-bcrypt
```

Python'da çoklu iş parçacıklı ve çoklu işlemli işlemleri kolaylaştırmak için kullanılan joblib kütüphanesini yükleyelim.
```sh
pip install joblib
```
Makine öğrenimi algoritmalarını ve araçlarını içeren scikit-learn kütüphanesini yükleyelim.
```sh
pip install scikit-learn
```
#### Projeyi çalıştırma

```sh
flask run --host=0.0.0.0
```

Projeye erişmek için Port sekmesinden 5000 portuna gidelim

Karşınızda Login ekranı açıldıysa tebrikler , projeyi başarılı bir şekilde çalıştırdınız. 

Haydi şimdi de projemizi deneyelim  ✨
