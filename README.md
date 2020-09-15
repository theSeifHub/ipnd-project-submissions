# Pixel Art Maker Project

## Table of Contents

* [Project Description](#project-description)
* [Udacity Instructions](#udacity-instructions)

## Project Description
You’ll build a single-page web app that allows users to draw pixel art on a customizable canvas.

You're given starter code, including HTML and CSS, to build the application. You'll write JavaScript code that lets the user create a grid of squares representing their design, and apply colors to those squares to create a digital masterpiece!

Your users should be able to:

* Dynamically set the size of the table as an _N_ by _M_ grid.
* Choose a color.
* Click a cell in the grid to fill that cell with the chosen color.

To get started, open `designs.js` from [starter code](https://github.com/udacity/project-pixel-art-maker-starter/archive/master.zip) and start building out the app's functionality.

## [Udacity](https://www.udacity.com) Instructions
Before writing any code, try loading up index.html from the starter project to see how things look! Notice that the design.js file is implemented in the <body> tag in the index.html file. Your goal is to build out the design.js file to achieve all the interactive elements on the page!

Open up design.js. As you start writing your code, keep these three tasks in mind:

1. Define your variables by selecting the DOM elements that the user will interact with. This is where your JavaScript variables can come into play! For instance, the submit button, the table, and the color picker need to be accessed. The value of the color selected needs to be stored as well, since the clicked cell in the table needs to be set to the selected color.
2. Add event listeners to the relevant DOM elements, so that user input can be color values and table sizes can be dynamically set by the user.
3. Set the size of the cross stitch canvas as an _N_ by _M_ grid with the makeGrid() function. Use your knowledge of JavaScript loops to dynamically clear and create the table based on user input. Each cell should have an event listener that sets the background color of the cell to the selected color.

Now test it! When you're done, you should be able to create a canvas of any size, choose a color using the color picker, and click on the canvas's table cells to set their color.


#### Project submitted and passed the review.
#### [Graduated](https://confirm.udacity.com/JHJYNSLG) the nanodegree program sucessfully on November 11, 2018