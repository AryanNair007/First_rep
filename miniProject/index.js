let message = "Let's Begin";
let gameOver = false, xTurn = true, vsPlayer = true;
let playerSign = '', computerSign = '', currentSign = '';


let headEl = document.querySelector('h1');
let boxesEl = document.querySelectorAll('.board-el');
let messageEl = document.querySelector('.message-el');
let vsCompEl = document.querySelector('#button-1');
let vsPersonEl = document.querySelector('#button-2');

//MODEL
let array = ["","","","","","","","",""];

const addElement = (boxNumber, value) => {
    array[boxNumber-1] = value;
}
const resetArray = () => {
    array = ["","","","","","","","",""];
}

//VIEW
const render = () => {
    for(let i = 1; i <= array.length; i++){
        let val = `.box-${i}`;
        let boxEl = document.querySelector(val);
        boxEl.textContent = array[i-1];
    }
}


//CONTROLLER
function setup(){
    resetArray();

    if(xTurn) {
        playerSign = 'X';
        computerSign = 'O';
    }
    else {
        playerSign = 'O';
        computerSign = 'X';
    }
    currentSign = playerSign;
    
    headEl.addEventListener('click', () =>{ 
        xTurn = (xTurn === true )? false: true;
    });
    vsCompEl.addEventListener('click', () => vsPlayer = (vsPlayer === true)? false: true);
    vsPersonEl.addEventListener('click', () => vsPlayer = (vsPlayer === true)? false: true);
    boxesEl.forEach(elem => {
        elem.addEventListener('click', loop);
    });
    
}

const loop = (elem) =>{
    if(gameOver === true) {
        gameOver = false;
        message = "Let's Begin";
        setup();
    }

    let classNameHolder = elem.target.className;
    let boxNumber = parseInt(classNameHolder.split('-')[1].split(' ')[0]);
    if(array[boxNumber-1] === '') addElement(boxNumber, currentSign);
    else return;

    if(vsPlayer) currentSign = (currentSign !== playerSign)? playerSign: computerSign; 
    else {
        computerPlay();
    }
    render();
    checkState();
    messageEl.textContent = message;
}

const checkState = () =>{
    if(checkWin(playerSign)){
        message = 'You Won!';
        gameOver = true;
    }else if(checkWin(computerSign)){
        message = 'Better Luck Next Time!';
        gameOver = true;
    }else if(checkDraw()){
        message = "It's Draw"
        gameOver = true;
    }
    return message
}

const checkWin = (playerSign) => {
    let len = 3;
    //checks the rows, coloums, leading diagonal and then the trainling diagonal respectively
    for(let i = 0; i < len; i++){
        if(areEqual(array[i*len], array[i*len+1], array[i*len+2], playerSign)) return true;
    }
    for(let i = 0; i < len; i++){
        if(areEqual(array[i], array[len+i], array[2*len+i], playerSign)) return true;
    }
    if(areEqual(array[0], array[4], array[8], playerSign)) return true;
    else if (areEqual(array[2], array[4], array[6], playerSign)) return true;
    else return false;
}
const checkDraw = () =>  {
    for(let i = 0; i < array.length; i++) {
        if(array[i] === "") return false;
    }
    return true;
}
const areEqual = (char1, char2, char3, playerSign) => char1 === char2 && char2 === char3 && char3 === playerSign

const computerPlay = () => {
    let choices = [];
    for(let i = 0; i < array.length; i++){
        if(array[i] === '') choices.push(i);
    }
    let choosedNumber = Math.floor(Math.random()*choices.length);
    console.log(choices, choices[choosedNumber])
    addElement(choices[choosedNumber]+1, computerSign);
}

setup();