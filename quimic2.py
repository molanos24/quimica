<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Ejercicio de Neutralización</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f4f8;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .card {
      background: white;
      padding: 2rem;
      border-radius: 1rem;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
      width: 100%;
      max-width: 400px;
    }

    h1 {
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    p {
      margin-bottom: 1rem;
    }

    input {
      width: 100%;
      padding: 0.5rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 0.5rem;
      margin-bottom: 1rem;
    }

    button {
      padding: 0.5rem 1rem;
      font-size: 1rem;
      border: none;
      border-radius: 0.5rem;
      margin-right: 0.5rem;
      cursor: pointer;
    }

    .check {
      background-color: #3b82f6;
      color: white;
    }

    .new {
      background-color: #6b7280;
      color: white;
    }

    .result {
      margin-top: 1rem;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Neutralización de Gas Lacrimógeno</h1>
    <p id="question">Cargando ejercicio...</p>
    <input type="number" id="answerInput" placeholder="Tu respuesta en gramos" />
    <div>
      <button class="check" onclick="checkAnswer()">Verificar</button>
      <button class="new" onclick="generateExercise()">Nuevo Ejercicio</button>
    </div>
    <div class="result" id="result"></div>
  </div>

  <script>
    let gasAmount = 0;

    function generateExercise() {
      gasAmount = Math.floor(Math.random() * 91) + 10; // entre 10 y 100g
      document.getElementById('question').innerText =
        ¿Cuántos gramos de compuesto neutralizante se necesitan para neutralizar ${gasAmount}g de gas lacrimógeno?;
      document.getElementById('answerInput').value = '';
      document.getElementById('result').innerText = '';
    }

    function checkAnswer() {
      const input = document.getElementById('answerInput').value;
      const userAnswer = parseFloat(input);

      if (isNaN(userAnswer)) {
        document.getElementById('result').innerText = "⚠️ Ingresa un número válido.";
        return;
      }

      // Suponemos una relación 1:1 en gramos para simplificar
      if (Math.abs(userAnswer - gasAmount) <= 1) {
        document.getElementById('result').innerText = "✅ ¡Correcto!";
      } else {
        document.getElementById('result').innerText = ❌ Incorrecto. La respuesta correcta es aproximadamente ${gasAmount}g.;
      }
    }

    // Inicia con un ejercicio
    generateExercise();
  </script>
</body>
</html>
