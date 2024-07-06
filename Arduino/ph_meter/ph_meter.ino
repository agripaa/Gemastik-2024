#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Konfigurasi LCD
LiquidCrystal_I2C lcd(0x27, 16, 2); // Alamat I2C dan ukuran LCD

// Pin untuk pH dan suhu
const int ph_pin = A0;
const int temp_pin = A1; // Temperature output dari modul pH ke pin analog A1

// Variabel untuk pH
float Po = 0;
float PH_step;
int nilai_analog_PH;
double TeganganPH;
const int voltase_ard = 5;
const float pH4 = 3.47;
const float pH7 = 3.77;

// Fungsi untuk mengkonversi tegangan suhu ke Celsius berdasarkan kalibrasi dua titik
float convertVoltageToTemperature(float voltage) {
  // Asumsi dua titik kalibrasi
  float voltage25C = 3.80; // Tegangan pada suhu 25°C
  float temperature25C = 25.0; // Suhu referensi 25°C dalam Celsius
  float voltage50C = 2.94; // Tegangan pada suhu 50°C
  float temperature50C = 50.0; // Suhu referensi 50°C

  // Menghitung kemiringan (slope) dari garis kalibrasi
  float m = (temperature50C - temperature25C) / (voltage50C - voltage25C);
  // Menghitung intercept (titik potong) dari garis kalibrasi
  float c = temperature25C - m * voltage25C;

  // Menghitung suhu berdasarkan tegangan yang dibaca
  return m * voltage + c;
}

void setup() {
  pinMode(ph_pin, INPUT);
  pinMode(temp_pin, INPUT);
  Serial.begin(9600);

  // Inisialisasi LCD
  lcd.init(); 
  lcd.begin(16, 2);
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("   Welcome to      ");
  lcd.setCursor(0, 1);
  lcd.print(" Circuit Digest    ");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Membaca nilai dari sensor pH
  nilai_analog_PH = analogRead(ph_pin);
  TeganganPH = voltase_ard / 1024.0 * nilai_analog_PH;
  PH_step = (pH7 - pH4) / 3;
  Po = 7.00 + ((pH4 - TeganganPH) / PH_step);

  // Membaca nilai dari sensor suhu
  int nilai_analog_temp = analogRead(temp_pin);
  float TeganganTemp = voltase_ard / 1024.0 * nilai_analog_temp;
  float suhu = convertVoltageToTemperature(TeganganTemp);

  // Menampilkan nilai pH dan suhu pada Serial Monitor
  Serial.print("Nilai pH: ");
  Serial.println(Po, 2);
  Serial.print("Suhu: ");
  Serial.println(suhu, 2);

  // Menampilkan nilai pH pada LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("pH: ");
  lcd.print(Po, 2);

  // Menampilkan nilai suhu pada LCD
  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(suhu, 2);
  lcd.print((char)223); // Simbol derajat
  lcd.print("C");

  delay(3000); // Tunggu 3 detik sebelum pembacaan berikutnya
}

// Check Voltase Modul
// int pH_Value;
// float Voltage;

// void setup() {
//   Serial.begin(9600);
//   pinMode(pH_Value, INPUT);
// }

// void loop() {
//   pH_Value = analogRead(A0);
//   Voltage = pH_Value * (5 / 1023.0);
//   Serial.println(Voltage);
//   delay(500); 
// }

