// Select color input
const colorPicker = document.querySelector('#colorPicker');


// Select size input
const sizePicker = document.querySelector('#sizePicker');
const inputHeight = document.querySelector('#inputHeight');
const inputWidth = document.querySelector('#inputWidth');


// When size is submitted by the user, call makeGrid()
const grid = document.querySelector('#pixelCanvas');
function makeGrid(evt) {
	evt.preventDefault();
	grid.innerHTML = '';
	let h = inputHeight.value;
	let w = inputWidth.value;
	// Create rows within the grid using Grid Height input
	for (let i = 0; i < h; i++) {
		const newRow = document.createElement('tr');
		// Create cells within each row using Grid Width input
		for (let j = 0; j < w; j++) {
			const newCell = document.createElement('td');
			newRow.appendChild(newCell);
		}
		grid.appendChild(newRow);
	}
}
sizePicker.addEventListener('submit', makeGrid);


// When a square in the grid is clicked, call paintCell()
function paintCell(evt) {
	if (evt.target.nodeName === 'TD') {
		evt.target.style.background = colorPicker.value;
	}
}
grid.addEventListener('click', paintCell);