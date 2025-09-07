import React, { useState } from "react";
import Upload from "./components/Upload";
import Suggestions from "./components/Suggestions";

function App() {
  const [faceShape, setFaceShape] = useState(null);
  const [suggestions, setSuggestions] = useState([]);

  return (
    <div className="p-6 text-center">
      <h1 className="text-3xl font-bold mb-4">Hairstyle Suggestion App</h1>
      <Upload setFaceShape={setFaceShape} setSuggestions={setSuggestions} />
      {faceShape && <Suggestions faceShape={faceShape} suggestions={suggestions} />}
    </div>
  );
}

export default App;
