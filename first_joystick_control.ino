int movement_switch_pin = 2;
int movement_x_pin = 0;
int movement_y_pin = 2;
int button_pin = 11;

int aim_switch_pin = 4;
int aim_x_pin = 3;
int aim_y_pin = 5;

int current = LOW;

int distance_to_up(int x, int y){
  return abs(x - 0) + abs(y - 510);  
}

int distance_to_right(int x, int y){
  return abs(x - 510) + abs(y - 0);  
}

int distance_to_left(int x, int y){
  return abs(x - 510) + abs(y - 1023);  
}

int distance_to_down(int x, int y){
  return abs(x - 1023) + abs(y - 510);  
}

int distance_to_center(int x, int y){
  return abs(x - 494) + abs(y - 510);  
}

// up = (0, 510)
// right = (510, 0)
// left = (510, 1023)
// down = (1023, 510)
char distance_from_cords(int x, int y){
    int up = distance_to_up(x, y);
    int right = distance_to_right(x, y);
    int left = distance_to_left(x, y);
    int down = distance_to_down(x, y);
    int center = distance_to_center(x, y);

    int minVal = min(up, min(right, min(left, min(center, down))));

    if(minVal == up){
      return 'U';
    }else if(minVal == right){
      return 'R';  
    }else if(minVal == left){
      return 'L';  
    }else if(minVal == down){
      return 'D';
    }else{
      return 'C';  
    }
}

// east(right), west(left), origin(center)
char horizontal_distance_from_cords(int x, int y){
    int right = distance_to_right(x, y);
    int left = distance_to_left(x, y);
    int center = distance_to_center(x, y);

    int minVal = min(right, min(left, center));  

    if(minVal == right){
      return 'E';
    }else if(minVal == left){
      return 'W';  
    }else{
      return 'O';  
    }
}

boolean debounce_button(boolean last){
  int current = digitalRead(button_pin);
  if(current != last){
    delay(5);
    current = digitalRead(button_pin);  
  }
  return current;
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(movement_switch_pin, INPUT);
  digitalWrite(movement_switch_pin, HIGH);

  pinMode(aim_switch_pin, INPUT);
  digitalWrite(aim_switch_pin, HIGH);
  
  pinMode(button_pin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int read_button = digitalRead(button_pin);
  int last_current = current;
  current = debounce_button(last_current);
  
  if(last_current == LOW && current == HIGH){
    Serial.println('S');  
    while(current == HIGH){
      current = digitalRead(button_pin);  
    }
    delay(100);
  }
  
  int move_x_pos = analogRead(movement_x_pin);
  int move_y_pos = analogRead(movement_y_pin);
  Serial.println(distance_from_cords(move_x_pos, move_y_pos));
  delay(100);

  int aim_x_pos = analogRead(aim_x_pin);
  int aim_y_pos = analogRead(aim_y_pin);
  Serial.println(horizontal_distance_from_cords(aim_x_pos, aim_y_pos));
  delay(100);
}
