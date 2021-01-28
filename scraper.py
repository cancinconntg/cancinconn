dan  Yardım kampanyasının . TelegramClient içe aktarımı senkronize et  
dan  Yardım kampanyasının . tl . fonksiyonlar . iletiler  GetDialogsRequest'i içe  aktarır
dan  Yardım kampanyasının . tl . türler  InputPeerEmpty'yi içe  aktarır
 os , sys içe aktar
 yapılandırıcıyı içe aktar
 csv içe aktar
ithalat  zamanı

re = " \ 033 [1; 31d"
gr = " \ 033 [1; 32a"
cy = " \ 033 [1; 36a"

def  başlık ():
    baskı ( f "" "
{ re } ╔╦╗ { cy } ┌─┐┬ ┌─┐ { re } ╔═╗ ╔═╗ { cy } ┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{ Yeniden } ║ { cy } ├┤ │ ├┤ { yeniden } ║ ╦ ╚═╗ { cy } │ ├┬┘├─┤├─┘├┤ ├┬┘
{ re } ╩ { cy } └─┘┴─┘└─┘ { re } ╚═╝ ╚═╝ { cy } └─┘┴└─┴ ┴┴ └─┘┴└─
              Sürüm: 1.01
 { re } Youtube'da Termux Professor'e abone olun.
   { cy } www.youtube.com/c/TermuxProfessorYT
        "" " )

cpass  =  configparser . RawConfigParser ()
cpass . oku ( 'config.data' )

deneyin :
    api_id  =  cpass [ 'kredi' ] [ 'kimlik' ]
    api_hash  =  cpass [ 'kredi' ] [ 'karma' ]
    telefon  =  cpass [ 'kredi' ] [ 'telefon' ]
    client  =  TelegramClient ( telefon , api_id , api_hash )
 KeyError hariç :
    os . sistem ( 'temizle' )
    afiş ()
    print ( yeniden + "[!] önce python3 setup.py'yi çalıştırın !! \ n " )
    sys . çıkış ( 1 )

müşteri . bağlan ()
eğer  değil  istemci . is_user_authorized ():
    müşteri . send_code_request ( telefon )
    os . sistem ( 'temizle' )
    afiş ()
    müşteri . sign_in ( telefon , giriş ( gr + '[+] Kodu girin:' + re ))
 
os . sistem ( 'temizle' )
afiş ()
sohbetler  = []
last_date  =  Yok
chunk_size  =  200
gruplar = []
 
sonuç  =  müşteri ( GetDialogsRequest (
             offset_date = last_date ,
             ofset_id = 0 ,
             offset_peer = InputPeerEmpty (),
             limit = chunk_size ,
             karma  =  0
         ))
sohbetler . ext ( sonuç . sohbetler )
 
için  sohbet  içinde  sohbetler :
    deneyin :
         sohbet ederseniz . megagroup ==  Doğru :
            gruplar . ekle ( sohbet )
    hariç :
        devam et
 
print ( gr + '[+] Üyeleri kazımak için bir grup seçin:' + re )
i = 0
için  g  olarak  grupları :
    baskı ( gr + '[' + cy + str ( i ) + ']'  +  '-'  +  g . başlık )
    i + = 1
 
baskı ( '' )
g_index  =  input ( gr + "[+] Bir Sayı Girin:" + re )
target_group = gruplar [ int ( g_index )]
 
print ( gr + '[+] Üyeler Getiriliyor ...' )
zaman . uyku ( 1 )
all_participants  = []
all_participants  =  müşteri . get_participants ( hedef_grup , agresif = Doğru )
 
print ( gr + '[+] Dosyaya Kaydediliyor ...' )
zaman . uyku ( 1 )
ile  açık ( "members.csv" , "W" , kodlayan = 'UTF-8' ) olarak  f :
    writer  =  csv . yazar ( f , sınırlayıcı = "," , çizgi sonlandırıcı = " \ n " )
    yazar . writerow ([ 'kullanıcı adı' , 'kullanıcı kimliği' , 'erişim karması' , 'ad' , 'grup' , 'grup kimliği' ])
    için  kullanıcı  içinde  all_participants :
        eğer  kullanıcı . kullanıcı adı :
            kullanıcı adı =  kullanıcı . Kullanıcı adı
        başka :
            kullanıcı adı =  ""
        eğer  kullanıcı . first_name :
            first_name =  kullanıcı . İsim
        başka :
            first_name =  ""
        eğer  kullanıcı . last_name :
            last_name =  kullanıcı . Soyadı
        başka :
            last_name =  ""
        adı = ( first_name  +  '  +  last_name ). şerit ()
        yazar . writerow ([ kullanıcı adı , kullanıcı . kimlik , kullanıcı . erişim_hash , ad , hedef_grup . başlık , hedef_grup . kimlik ])      
print ( gr + '[+] Üyeler başarıyla toplandı. Üye Eklemek İçin Termux Professor Youtube Kanalına Abone Olun' )
