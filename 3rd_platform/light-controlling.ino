// Khai báo chân kết nối cho 3 đèn LED
const int led1 = 2; // LED 1 gắn vào chân số 2
const int led2 = 3; // LED 2 gắn vào chân số 3
const int led3 = 4; // LED 3 gắn vào chân số 4
int valor_data = 0;
void setup() {
  // Đặt các chân LED làm đầu ra
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  digitalWrite (led1, LOW);
  digitalWrite (led2, LOW);
  digitalWrite (led3, LOW);
  Serial.begin(9600);
  Serial.println("Đã kết nối");
}

void loop() {
  // // Bật LED 1 và tắt các LED khác
  // digitalWrite(led1, HIGH);
  // digitalWrite(led2, LOW);
  // digitalWrite(led3, LOW);
  // delay(1000); // Giữ sáng trong 1 giây

  // // Bật LED 2 và tắt các LED khác
  // digitalWrite(led1, LOW);
  // digitalWrite(led2, HIGH);
  // digitalWrite(led3, LOW);
  // delay(1000); // Giữ sáng trong 1 giây

  // // Bật LED 3 và tắt các LED khác
  // digitalWrite(led1, LOW);
  // digitalWrite(led2, LOW);
  // digitalWrite(led3, HIGH);
  // delay(1000); // Giữ sáng trong 1 giây


  while(Serial.available()){
    valor_data= Serial.read();
  }
  if (valor_data == '1') {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }
  if (valor_data == '2') {
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
  }
  if (valor_data == '3') {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
  }
  if (valor_data == '4') {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }
  if (valor_data == '5'|| valor_data == '0') {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
  }
}
