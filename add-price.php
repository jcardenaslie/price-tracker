<?php
function DBConnect(){
    // Create connection
    global $servername, $username, $password, $dbname;
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully <br>";

    return $conn;

}

function DBInsert($conn, $sql){
    // Insert Data
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully <br>";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

function DBClose($conn){
    $conn->close();
}
?>

<?php
$servername = "sql104.epizy.com";
$username = "epiz_24700975";
$password = "2V3T8b23nxP0h";
$dbname = "epiz_24700975_priceTracker";

$conn;

$price = $_GET['price'];
$book_name = $_GET['name'];

echo "Hola Mundo <br>";

if (isset($price) && isset($book_name)){
    echo "{$book_name} {$price} <br>";
    $conn = DBConnect();
    $sql = "INSERT INTO price (price, product_name) VALUES ({$price}, '{$book_name}')";
    DBInsert($conn, $sql);
    DBClose($conn);
} else {
    echo "No data passed.";
}

?>