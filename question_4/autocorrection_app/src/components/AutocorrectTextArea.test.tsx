import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import { AutocorrectTextArea } from "./AutocorrectTextArea";
import {IncorrectWordsEnum, RightWordsEnum, WHITE_SPACE} from "../constants/AutocorrectTextArea";

describe("AutocorrectTextArea", () => {
  let textarea: HTMLTextAreaElement;

  const renderComponent = (text: string) => {
    render(<AutocorrectTextArea />);
    textarea = screen.getByTestId("textarea");
    fireEvent.change(textarea, { target: { value: text } });
  }


  test("should update text state on text change", () => {
    const text = "Hello, world! ";
    renderComponent(text)
    expect(textarea.value).toBe(text );
  });

  test("should autocorrect the last word on space key press", () => {
    renderComponent(IncorrectWordsEnum.HI + WHITE_SPACE )
    expect(textarea.value).toBe(RightWordsEnum.HI + WHITE_SPACE);
  });

  test("should not autocorrect the last word on non-space key press", () => {
    const text = "Hello";
    renderComponent(text)
    expect(textarea.value).toBe(text);
  });
});
