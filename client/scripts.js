const canvas = document.getElementById("canvas");
const clear = document.getElementById("clear")
const ctx = canvas.getContext("2d");

const TRANSLATED_WIDTH = 92;
const PIXEL_WIDTH = Math.floor(canvas.width / TRANSLATED_WIDTH);
const CANVAS_WIDTH = PIXEL_WIDTH * TRANSLATED_WIDTH

console.log(canvas.width)
console.log(TRANSLATED_WIDTH)
console.log(PIXEL_WIDTH)
console.log(CANVAS_WIDTH)

let isPainting = false;
let lineWidth = 2;
let startX;
let startY;
let data = new Array();

clear.addEventListener("click", e => {
    if (e.target.id === "clear") {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        data = new Array();
    }
});

canvas.addEventListener('mousedown', (e) => {
    isPainting = true;
    const xPixel = Math.floor((e.clientX - canvas.offsetLeft) / PIXEL_WIDTH);
    const yPixel = Math.floor((e.clientY - canvas.offsetTop) / PIXEL_WIDTH);
    data[((xPixel - 1) * TRANSLATED_WIDTH + yPixel) - 1] = 1;

    console.log("drawing at " + xPixel + " " + yPixel)
    ctx.fillStyle = 'white';
    ctx.fillRect(xPixel * PIXEL_WIDTH, yPixel * PIXEL_WIDTH, PIXEL_WIDTH, PIXEL_WIDTH);
});

canvas.addEventListener('mouseup', (e) => {
    isPainting = false;
});

canvas.addEventListener('mousemove', (e) => {
    if (!isPainting) {
        return;
    }
    const xPixel = Math.floor((e.clientX - canvas.offsetLeft) / PIXEL_WIDTH);
    const yPixel = Math.floor((e.clientY - canvas.offsetTop) / PIXEL_WIDTH);
    data[((xPixel - 1) * TRANSLATED_WIDTH + yPixel) - 1] = 1;

    console.log("drawing at " + xPixel + " " + yPixel)
    ctx.fillStyle = 'white';
    ctx.fillRect(xPixel * PIXEL_WIDTH, yPixel * PIXEL_WIDTH, PIXEL_WIDTH, PIXEL_WIDTH);
});