import { Result } from './result'

export interface ResultPage {
  prevPage : string,
  nextPage : string,
  results : [Result]
}
