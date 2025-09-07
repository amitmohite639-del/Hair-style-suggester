import React from "react";

function Upload({ setFaceShape, setSuggestions }) {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("YOUR_BACKEND_URL/upload", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    setFaceShape(data.face_shape);
    setSuggestions(data.suggestions);
  };

  return (
    <div>
      <input type="file" accept="image/*" onChange={handleUpload} />
    </div>
  );
}

export default Upload;
