import React from "react";

function Suggestions({ faceShape, suggestions }) {
  return (
    <div className="mt-4">
      <h2 className="text-xl font-semibold">Detected Face Shape: {faceShape}</h2>
      <h3 className="mt-2">Recommended Hairstyles:</h3>
      <ul className="list-disc list-inside">
        {suggestions.map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ul>
    </div>
  );
}

export default Suggestions;
