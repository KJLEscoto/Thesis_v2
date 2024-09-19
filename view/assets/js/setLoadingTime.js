function random(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const randomTimer = random(400, 1500);

export const timer = randomTimer;


