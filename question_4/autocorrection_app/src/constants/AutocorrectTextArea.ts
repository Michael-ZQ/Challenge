export const WHITE_SPACE = " ";
export enum IncorrectWordsEnum {
  HI = "ho",
  IAM = "iam",
  DEVELOPER = "develper",
  REALLY = "realy",
  LIKE = "liki",
  COFFEE = "cofee",
}

export enum RightWordsEnum {
  HI = "Hi",
  IAM = "I'm",
  DEVELOPER = "developer",
  REALLY = "really",
  LIKE = "like",
  COFFEE = "coffee",
}

export const DICTIONARY: Record<string, string> = {
  [IncorrectWordsEnum.HI]: RightWordsEnum.HI,
  [IncorrectWordsEnum.IAM]: RightWordsEnum.IAM,
  [IncorrectWordsEnum.DEVELOPER]: RightWordsEnum.DEVELOPER,
  [IncorrectWordsEnum.REALLY]: RightWordsEnum.REALLY,
  [IncorrectWordsEnum.LIKE]: RightWordsEnum.LIKE,
  [IncorrectWordsEnum.COFFEE]: RightWordsEnum.COFFEE,
};
