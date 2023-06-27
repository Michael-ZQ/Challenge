import React from "react";
import "./App.css";
import { AutocorrectTextArea } from "../components/AutocorrectTextArea";
import { AppLabelsEnum } from "../constants/AppLabelsEnum";

function App() {
  return (
    <div className="App">
      <header className="App-header">{AppLabelsEnum.TITLE}</header>

      <AutocorrectTextArea />
      <span>Type text: {AppLabelsEnum.EXAMPLE_TEXT} </span>
    </div>
  );
}

export default App;
