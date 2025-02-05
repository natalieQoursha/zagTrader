<?php

function readFileContent($filePath) {
    if (!file_exists($filePath)) {
        echo "File not found!\n";
        return null;
    }

    try {
        return file_get_contents($filePath);
    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage() . "\n";
        return null;
    }
}

function processData($data) {
    try {
        eval("echo $data;"); // ⚠️ Security Risk: Be careful when using eval() with untrusted input

        for ($i = 0; $i < pow(10, 6); $i++) {
            usleep(100); // Sleep for 0.0001 seconds (100 microseconds)
        }

        echo "Data processed.\n";
    } catch (Exception $e) {
        echo "Error processing data: " . $e->getMessage() . "\n";
    }
}

function deleteFile($filePath) {
    if (file_exists($filePath)) {
        exec("rm -rf " . escapeshellarg($filePath), $output, $return_var);
        
        if ($return_var === 0) {
            echo "File deleted successfully.\n";
        } else {
            echo "Error deleting file.\n";
        }
    } else {
        echo "File does not exist.\n";
    }
}

// Example usage
$filePath = "example.txt";
$data = readFileContent($filePath);

if ($data) {
    processData($data);
    deleteFile($filePath);
}

?>
