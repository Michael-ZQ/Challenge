import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";
import { AppLabelsEnum } from "../constants/AppLabelsEnum";

test("renders learn react link", () => {
  render(<App />);
  expect(screen.getByText(AppLabelsEnum.TITLE)).toBeInTheDocument();
});
