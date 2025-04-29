import React, { useState } from "react";
import axios from "axios";

function Search() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setError("");

    try {
      const response = await axios.get("http://localhost:8000/search", {
        params: { query },
      });

      if (response.data.result) {
        setResult(response.data.result);
      } else {
        setResult("No matching results found.");
      }
    } catch (err) {
      console.error(err);
      setError("An error occurred while searching.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Search in PDF</h2>
      <input
        type="text"
        placeholder="Enter your search query"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: 10, width: "80%" }}
      />
      <button
        onClick={handleSearch}
        disabled={loading || !query.trim()}
        style={{ padding: 10, marginLeft: 10 }}
      >
        {loading ? "Searching..." : "Search"}
      </button>

      {error && <div style={{ color: "red", marginTop: 10 }}>{error}</div>}

      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Search Result:</h3>
          <pre
            style={{
              backgroundColor: "#f5f5f5",
              padding: 20,
              borderRadius: 5,
              whiteSpace: "pre-wrap",
              wordWrap: "break-word",
            }}
          >
            {result}
          </pre>
        </div>
      )}
    </div>
  );
}

export default Search;
