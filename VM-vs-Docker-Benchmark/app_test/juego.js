let blocks = [];
let spikes = [];
let players = [];
let populationSize = 5;
let brains = [];
let generation = 1;
let levelLength = 2000;
let gameSpeed = 5;

let bestBrain = [];
let bestDistance = 0;

let editorMode = true;
let camOffsetX = 0;
let isDragging = false;
let dragStartX;

let fpsCounter = 0;
let fpsTimer = 0;
let actualFPS = 0;

let genStartTime = 0;
let lastGenDuration = 0;
let avgSteps = 0;

function setup() {
  createCanvas(800, 400);
  initLevel();
  initPopulation();
  fpsTimer = millis();
}

function draw() {
  background(30);

  if (editorMode) {
    drawEditor();
    return;
  }

  let allDead = true;
  let cameraX = 0;

  for (let p of players) {
    if (p.alive) {
      p.update();
      allDead = false;
    }
    cameraX = max(cameraX, p.x);
  }

  cameraX -= 100;
  push();
  translate(-cameraX, 0);

  drawGround();
  for (let b of blocks) b.show();
  for (let s of spikes) s.show();
  for (let p of players) p.show();

  pop();

  fill(255);
  textSize(16);
  text(`Gen: ${generation}`, 10, 20);
  text(`Best: ${nf(bestDistance, 1, 0)}`, 10, 40);
  text(`Presiona 'E' para editar nivel`, 10, 60);

  fpsCounter++;
  if (millis() - fpsTimer > 1000) {
    actualFPS = fpsCounter;
    fpsCounter = 0;
    fpsTimer = millis();
  }

  text(`FPS: ${actualFPS}`, 10, 80);
  text(`Gen Time: ${nf(lastGenDuration / 1000, 1, 2)}s`, 10, 100);
  text(`Avg Steps: ${nf(avgSteps, 1, 0)}`, 10, 120);

  if (allDead) nextGeneration();
}

function drawEditor() {
  background(50);
  push();
  translate(-camOffsetX, 0);
  drawGround();
  for (let b of blocks) b.show();
  for (let s of spikes) s.show();
  pop();

  fill(255);
  textSize(16);
  text("Editor de nivel (Click izq = bloque, Click der = spike)", 10, 20);
  text("Arrastra para mover el nivel", 10, 40);
  text("Presiona 'E' para iniciar simulación", 10, 60);
  text("Presiona 'S' para guardar nivel", 10, 80);
}

function mousePressed() {
  if (!editorMode) return;

  if (mouseButton === CENTER) return false;

  isDragging = true;
  dragStartX = mouseX;
  return false;
}

function mouseReleased() {
  isDragging = false;

  if (!editorMode) return;

  let gridX = floor((mouseX + camOffsetX) / 40) * 40;
  let gridY = floor(mouseY / 40) * 40;

  if (mouseButton === LEFT) {
    blocks.push(new Block(gridX, gridY));
  } else if (mouseButton === RIGHT) {
    spikes.push(new Spike(gridX, gridY));
  }
}

function mouseDragged() {
  if (editorMode && isDragging) {
    let dx = pmouseX - mouseX;
    camOffsetX = constrain(camOffsetX + dx, 0, levelLength - width);
  }
}

function keyPressed() {
  if (key === 'E') {
    editorMode = !editorMode;
    if (!editorMode) initPopulation();
  }

  if (key === 'S' && editorMode) {
    console.log("=== BLOQUES ===");
    for (let b of blocks) console.log(`blocks.push(new Block(${b.x}, ${b.y}));`);
    console.log("=== SPIKES ===");
    for (let s of spikes) console.log(`spikes.push(new Spike(${s.x}, ${s.y}));`);
  }
}

function initLevel() {
  blocks = [];
  spikes = [];
  for (let x = 0; x < levelLength; x += 40) {
    blocks.push(new Block(x, height - 40));
  }
}

function drawGround() {
  fill(40);
  rectMode(CORNER);
  rect(0, height - 40, levelLength, 40);
}

function initPopulation() {
  players = [];
  brains = [];
  genStartTime = millis();

  for (let i = 0; i < populationSize; i++) {
    let brain = bestBrain.length > 0 ? mutate([...bestBrain]) : [];
    brains.push(brain);
    players.push(new Player(brain));
  }
}

function nextGeneration() {
  let bestPlayer = null;
  let furthest = 0;

  for (let p of players) {
    if (p.x > furthest) {
      furthest = p.x;
      bestPlayer = p;
    }
  }

  if (furthest > bestDistance) {
    bestDistance = furthest;
    bestBrain = [...bestPlayer.brain];
  }

  generation++;
  lastGenDuration = millis() - genStartTime;
  let totalSteps = 0;
  for (let p of players) totalSteps += p.step;
  avgSteps = totalSteps / players.length;

  console.log(`Gen ${generation} | Time: ${lastGenDuration}ms | Avg Steps: ${avgSteps} | FPS: ${actualFPS}`);

  initPopulation();
}

function mutate(brain) {
  for (let i = 0; i < brain.length; i++) {
    if (random() < 0.1) brain[i] = !brain[i];
  }
  return brain;
}

class Block {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  show() {
    fill(0, 100, 200);
    rect(this.x, this.y, 40, 40);
  }
}

class Spike {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  show() {
    fill(255, 0, 0);
    triangle(this.x, this.y + 40, this.x + 20, this.y, this.x + 40, this.y + 40);
  }

  hits(p) {
    return (
      p.x + p.w > this.x &&
      p.x < this.x + 40 &&
      p.y + p.h > this.y &&
      p.y < this.y + 40
    );
  }
}

class Player {
  constructor(brain = []) {
    this.x = 50;
    this.y = height - 60;
    this.w = 30;
    this.h = 30;
    this.ySpeed = 0;
    this.onGround = false;
    this.jumpCooldown = 0;
    this.alive = true;
    this.brain = brain;
    this.step = 0;
  }

  update() {
    if (!this.alive) return;

    this.x += gameSpeed;
    this.ySpeed += 1;
    this.y += this.ySpeed;

    this.onGround = false;
    for (let b of blocks) {
      if (
        this.x + this.w > b.x &&
        this.x < b.x + 40 &&
        this.y + this.h > b.y &&
        this.y + this.h < b.y + 20
      ) {
        this.y = b.y - this.h;
        this.ySpeed = 0;
        this.onGround = true;
      }
    }

    for (let s of spikes) {
      if (s.hits(this)) this.alive = false;
    }

    if (this.y > height) this.alive = false;

    if (this.step >= this.brain.length) {
      this.brain.push(random() < 0.1);
    }

    if (this.brain[this.step] && this.onGround && this.jumpCooldown <= 0) {
      this.jump();
    }

    this.step++;
    this.jumpCooldown--;
  }

  jump() {
    this.ySpeed = -15;
    this.jumpCooldown = 10;
    this.onGround = false;
  }

  show() {
    fill(this.alive ? color(0, 255, 255) : color(100));
    rect(this.x, this.y, this.w, this.h);
  }
}
