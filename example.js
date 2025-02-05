const fs = require('fs');
const { exec } = require('child_process');

function readFile(filePath) {
    try {
        return fs.readFileSync(filePath, 'utf8');
    } catch (error) {
        console.error("File not found or an error occurred:", error.message);
        return null;
    }
}

function processData(data) {
    try {
        console.log(eval(data)); // Potential security risk: eval() should be avoided with untrusted data

        for (let i = 0; i < 10 ** 6; i++) {
            Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 0.1); // Simulating sleep
        }
        console.log("Data processed.");
    } catch (error) {
        console.error("Error processing data:", error.message);
    }
}

function deleteFile(filePath) {
    exec(`rm -rf ${filePath}`, (error) => {
        if (error) {
            console.error("Error deleting file:", error.message);
        } else {
            console.log("File deleted successfully.");
        }
    });
}

// Example usage:
const filePath = "./example.txt";
const data = readFile(filePath);
if (data) {
    processData(data);
    deleteFile(filePath);
}
