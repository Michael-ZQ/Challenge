import React, { ChangeEvent, useState } from "react";
import { DICTIONARY, WHITE_SPACE } from "../constants/AutocorrectTextArea";

const styles = () => ({
  text: {
    width: "700px",
    height: "300px",
    fontSize: "25px",
  },
});
export const AutocorrectTextArea: React.FC = () => {
  const classes = styles();
  const [text, setText] = useState<string>("");

  const handleTextChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
    const inputValue = event.target.value;
    const lastCharacter = inputValue[inputValue.length - 1];

    if (lastCharacter === WHITE_SPACE) {
      setText(correctLastWord(inputValue));
    } else {
      setText(inputValue);
    }
  };

  const correctLastWord = (inputValue: string) => {
    const words = inputValue.trim().split(WHITE_SPACE);
    const lastWord = words[words.length - 1];

    words[words.length - 1] = DICTIONARY[lastWord] || lastWord;

    return words.join(WHITE_SPACE) + WHITE_SPACE;
  };

  return (
    <div>
      <textarea
        data-testid="textarea"
        style={classes.text}
        value={text}
        onChange={handleTextChange}
      />
    </div>
  );
};
