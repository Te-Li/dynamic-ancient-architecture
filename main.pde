//20240509LT


PImage img;
PVector[] points;
PVector[] targets;
int numPoints = 80000; // 彩色点数量

float[] sizes; 
PFont font;


void setup() {

  size(800, 600);
  img = loadImage("司马温公祠.png");
  img.resize(width, height);
  points = new PVector[numPoints];
  targets = new PVector[numPoints];
  sizes = new float[numPoints]; // 初始化粒子大小数组

  for (int i = 0; i < numPoints; i++) {
    points[i] = new PVector(random(width), random(height));
    targets[i] = new PVector(random(width), random(height));
    // 每个粒子随机分配大小
    sizes[i] = random(3, 9);
  }
  background(0);


  //PFont.list();
  /*
  println("当前程序的路径是: " + sketchPath());
   noLoop(); // 只运行一次setup
   */
}


void draw() {
  background(0);
  for (int i = 0; i < numPoints; i++) {
    // 插值
    points[i].x = lerp(points[i].x, targets[i].x, 0.05);
    points[i].y = lerp(points[i].y, targets[i].y, 0.05);

    // 获取粒子位置的颜色
    int imgColor = img.get(int(targets[i].x), int(targets[i].y));
    fill(imgColor);
    noStroke();
    if (imgColor==0) {
      continue;
    }
    ellipse(points[i].x, points[i].y, sizes[i], sizes[i]);
  }

  font = createFont("方正大标宋_GBK", 48);
  textFont(font);

  fill(255);
  textAlign(LEFT, LEFT); 

  text("司 马 温 公 祠", width / 12, height / 5);

  font = createFont("方正大标宋_GBK", 24);
  textFont(font);
  fill(255); 
  textAlign(LEFT, LEFT); 
  text("\n5月20日——————————5月25日", width / 12, 7*height / 8);

  font = createFont("方正大标宋_GBK", 24);
  textFont(font);
  fill(255); 
  textAlign(RIGHT, RIGHT); 
  text("CAUP × 山西文旅\n运城古建行", 11*width / 12, 7*height / 8);


  font = createFont("华光行草_CNKI", 120);
  textFont(font);
  fill(255, 100); 
  textAlign(CENTER, CENTER); 
  text("夏县", width / 2, height / 2);


  saveFrame("output15/frame-####.png");
}

void keyPressed() {
  if (key == 's') {
    exit(); // 按 's' 停止
  }
}

void mouseClicked() {
  for (int i = 0; i < numPoints; i++) {
    targets[i] = new PVector(random(width), random(height));
    sizes[i] = random(3, 9); 
  }
}
