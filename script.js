const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");
const btn3 = document.getElementById("btn3");
const btn4 = document.getElementById("btn4");
const btn5 = document.getElementById("btn5");
const btn6 = document.getElementById("btn6");
const btn7 = document.getElementById("btn7");
const btn8 = document.getElementById("btn8");
const btn9 = document.getElementById("btn9");
const label = document.getElementById("label");
let gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0];

let turn = 1;
function move(btn, n) {
    if (btn.textContent != "") {
        return;
    }
    if (turn == 1) {
        gameBoard[n] = 1;
        btn.textContent = "X";
        label.textContent = "Player O's Turn";
    } else {
        gameBoard[n] = 2;
        btn.textContent = "O";
        label.textContent = "Player X's Turn";
    }
    turn *= -1;
    check();
}

function reset() {
    turn = 1;
    gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    label.textContent = "Player X's Turn";
    btn1.textContent = "";
    btn2.textContent = "";
    btn3.textContent = "";
    btn4.textContent = "";
    btn5.textContent = "";
    btn6.textContent = "";
    btn7.textContent = "";
    btn8.textContent = "";
    btn9.textContent = "";
    enable_buttons();
}

function check() {
    const row1X = gameBoard[0] == 1 && gameBoard[1] == 1 && gameBoard[2] == 1;
    const row2X = gameBoard[3] == 1 && gameBoard[4] == 1 && gameBoard[5] == 1;
    const row3X = gameBoard[6] == 1 && gameBoard[7] == 1 && gameBoard[8] == 1;
    const col1X = gameBoard[0] == 1 && gameBoard[3] == 1 && gameBoard[6] == 1;
    const col2X = gameBoard[1] == 1 && gameBoard[4] == 1 && gameBoard[7] == 1;
    const col3X = gameBoard[2] == 1 && gameBoard[5] == 1 && gameBoard[8] == 1;
    const dia1X = gameBoard[0] == 1 && gameBoard[4] == 1 && gameBoard[8] == 1;
    const dia2X = gameBoard[2] == 1 && gameBoard[4] == 1 && gameBoard[6] == 1;

    const row1O = gameBoard[0] == 2 && gameBoard[1] == 2 && gameBoard[2] == 2;
    const row2O = gameBoard[3] == 2 && gameBoard[4] == 2 && gameBoard[5] == 2;
    const row3O = gameBoard[6] == 2 && gameBoard[7] == 2 && gameBoard[8] == 2;
    const col1O = gameBoard[0] == 2 && gameBoard[3] == 2 && gameBoard[6] == 2;
    const col2O = gameBoard[1] == 2 && gameBoard[4] == 2 && gameBoard[7] == 2;
    const col3O = gameBoard[2] == 2 && gameBoard[5] == 2 && gameBoard[8] == 2;
    const dia1O = gameBoard[0] == 2 && gameBoard[4] == 2 && gameBoard[8] == 2;
    const dia2O = gameBoard[2] == 2 && gameBoard[4] == 2 && gameBoard[6] == 2;

    if (row1X || row2X || row3X || col1X || col2X || col3X || dia1X || dia2X) {
        label.textContent = "Player X wins!";
        disable_buttons();

    } else if (row1O || row2O || row3O || col1O || col2O || col3O || dia1O || dia2O) {
        label.textContent = "Player O wins!";
        disable_buttons();
    } else if (gameBoard[0] != 0 && gameBoard[1] != 0 && gameBoard[2] != 0 && gameBoard[3] != 0 && gameBoard[4] != 0 && gameBoard[5] != 0 && gameBoard[6] != 0 && gameBoard[7] != 0 && gameBoard[8] != 0) {
        label.textContent = "Draw!";
        disable_buttons();
    }
}

function disable_buttons() {
    btn1.disabled = true;
    btn2.disabled = true;
    btn3.disabled = true;
    btn4.disabled = true;
    btn5.disabled = true;
    btn6.disabled = true;
    btn7.disabled = true;
    btn8.disabled = true;
    btn9.disabled = true;
}

function enable_buttons() {
    btn1.disabled = false;
    btn2.disabled = false;
    btn3.disabled = false;
    btn4.disabled = false;
    btn5.disabled = false;
    btn6.disabled = false;
    btn7.disabled = false;
    btn8.disabled = false;
    btn9.disabled = false;
}

