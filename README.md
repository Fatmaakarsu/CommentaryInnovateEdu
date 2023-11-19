# CommentaryInnovateEdu
Buluş Bilişimciler Eğitim Platformu Yorum Eklentisi Projesi

Projenin her aşamasının readme.md dosyaları "readme" klasörü içindedir.

# Buluş Bilişimciler Eğitim Platformu Yorum Eklentisi Projesi

## Proje motivasyonu

Merhabalar ✨

##### Biliyor muydunuz?
 

Araştırmalar özellikle başlangıç seviyesindeki kullanıcıların genellikle eğitim videolarınının puanından önce en fazla kullanıcı tarafından alınmış, değerlendirilmiş, eğitmen ve eğitimi alan kişiler arasında soru-cevap yoğunluğu en çok olan eğitimlere yöneldiğini gösteriyor.


Eğitim platformlarının her eğitim için yorum seçeneğini aktif etmesinin katkılarına bakalım:
- İkili İletişim ve Etkileşim: Yorum seçeneği, öğrencilerin eğitim içeriğiyle etkileşimde bulunmasına olanak tanır. Bu, öğrencilerin eğitim sürecini daha kişisel ve etkileşimli hale getirir.

- Topluluk Duygusu: Yorumlar, öğrenciler arasında bir topluluk duygusu oluşturabilir. Başlangıç seviyesindeki öğrenciler, benzer deneyimlere sahip diğerleriyle iletişim kurarak destek bulabilir ve sorularını sorabilir.

- Motivasyon ve Geri Bildirim: Yorumlar, öğrencilere geri bildirim sağlar. Başlangıç seviyesindeki öğrenciler için olumlu bir geri bildirim almak, motivasyonlarını artırabilir ve öğrenme sürecine olumlu bir etki yapabilir.

- Kolaylıkla Anlaşılabilirlik: Başlangıç seviyesindeki öğrenciler, belirli konularda karşılaştıkları zorlukları paylaşabilir ve diğer öğrencilerden yardım alabilir. Bu, öğrenme sürecinin daha anlaşılır ve etkili olmasına yardımcı olabilir.

- Eğitim İçeriğinin İyileştirilmesi: Yorumlar, eğitim içeriğini geliştirmek için değerli bilgiler sağlar. Öğrencilerin geri bildirimleri, eğitim sağlayıcılara hangi konuların daha iyi anlaşılması gerektiği veya hangi alanlarda iyileştirmeler yapılması gerektiği konusunda önemli içgörüler sunabilir.

- Soruların Yanıtlanması: Başlangıç seviyesindeki öğrenciler genellikle belirli konular hakkında soruları olabilir. Yorumlar, bu soruların yanıtlanmasına olanak tanır ve öğrencilere ek açıklamalar ve rehberlik sağlar.

Eğitim teknolojileri ve bilişim sektöründe lider konumda olan şirketler, kullanıcıların etkileşimde bulunmasını teşvik eden ve eğitim içeriğini geliştirmek için geri bildirimi değerlendiren sistemleri başarıyla kullanmaktadır.

Sektörde Bilgisayar bilimleri ve IT sektöründe en çok tercih edilen eğitim platformlarına bir bakalım:
![Alternatif Metin](https://github.com/Fatmaakarsu/project-task/blob/main/tablo11.png?raw=true)

Haydi gelin bizde beraber Bulut Bilişimciler platformu için geliştirdiğimiz yorum eklentisi projesini inceleyelim ✨

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

Karşınızda Login ekranı açıldıysa tebrikler 🙌 projeyi başarılı bir şekilde çalıştırdınız.  🙏


## Proje İnceleme
Yorum sistemini deneyebilmek için bir kullanıcı ile giriş yapmamız gerekmektedir.

> Örnek kullanıcı emaili : bulut23@gmail.com
> Şifre: bulut

Kullanıcı girişi olduktan sonra direkt olarak bir eğitim bölümü içindeki yorum sistemini görüyoruz.

Yorum sisteminin özelliklerini deneyebiliriz   ✨
- Kullanıcı yorum yaptığında yorum o kullanıcının kayıtlı username i ile yayınlanır
- Kullanıcı yorumları beğenebilir ve yorumlara cevap verebilir
- Bir kullanıcı bir yorumu maksimum 1 kez beğenebilir.
- Kullanıcı isterse anonim yorum seçeneğini seçerek kullanıcı adını gizleyebilir.
- Yorumlarda aranmak istenen anahtar kelimeler "Yorum ara" kısmına yazılarak kolayca erişilebilir.
- Kullanıcılar kötüye kullanım olarak gördükleri yorumları şikayet edebilir.
- Sorun Bildir / İstek Gönder butonu ile kullanıcılar Bulut Bilişimciler issue-tracker reposuna yönlendilir.

![image](https://github.com/Fatmaakarsu/CommentaryInnovateEdu/assets/79910837/289f6b58-475f-48e8-acb4-b8fc7a059028)

![image](https://github.com/Fatmaakarsu/CommentaryInnovateEdu/assets/79910837/55709456-73bf-441f-9d24-45252e9d8249)

## Sonuç

Harika ☺☺️☺️

Projemizle birlikte, buluş bilişimciler eğitim platformumuzda sunduğumuz yorum eklentisi, sektördeki öncülerden daha gelişmiş ve işlevsel hale geldi. Eğitime kaydolan herkes, eğitimlerden daha fazla verim elde edebilecek ve hızla ilerleme kaydedebilecekler. Gelişmiş özelliklerimiz, kullanıcıların eğitim içeriklerini daha etkili bir şekilde değerlendirmelerine, sorular sormalarına, cevap almalarına ve genel olarak daha interaktif bir öğrenme deneyimi yaşamalarına olanak tanıyacak. 

![Örnek Resim](https://github.com/Fatmaakarsu/project-task/blob/main/tablo2.png?raw=true)


### Proje getirileri

✅ Sürdürülebilir

✅ Kullanıcı deneyimini önemli ölçüde zenginleştirir

✅ Sitenin genel başarısına katkı sağlar






