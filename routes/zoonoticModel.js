const express = require('express');
const { spawn } = require('child_process');

const router = express.Router();

function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

router.post('/predict', (req, res) => {
    console.log(req.body)
    let data = [];
    for (const key of Object.keys(req.body)) {
        if (isNumeric(req.body[key])) {
            data.push(parseInt(req.body[key]));
        } else {
            data.push(req.body[key]);
        }
    }

    // res.send(data);


    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['program.py', 'African_green_monkey_polyomavirus', data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]]);
    // collect data from script
    python.stdout.on('data', function(data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });
});
module.exports = router;