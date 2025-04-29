import React, { useState } from "react";
import axios from "axios";
import Search from "./Search";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "http://localhost:8000/upload-pdf",
      formData
    );
    setText(response.data.text);
  };

  return (
    <div style={{ padding: 25 }}>
      <h2>AutoGenAI - Upload PDF</h2>
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload} disabled={!file}>
        Upload
      </button>
      <textarea value={text} rows="20" cols="80" readOnly />
      <Search />
    </div>
  );
}

export default App;
