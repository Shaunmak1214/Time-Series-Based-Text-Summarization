import { Model, Document } from 'mongoose';
import { QueryResult } from '../paginate/paginate';

export interface ISent {
  p_score: number;
  n_score: number;
  nu_score: number;
  comparative: number;
  tokens: string[];
  words: string[];
  positive: string[];
  negative: string[]; 
  neutral: string[];
}

export interface IAns {
  answer: string;
  tags: string[];
  upvotes: number;
  downvotes: number;
  sentiment: ISent;
}

export interface IFaq {
  question: string;
  answer: IAns[];
  tags: string[];
}

export interface IFaqDoc extends IFaq, Document {}

export interface IFaqModel extends Model<IFaqDoc> {
  paginate(filter: Record<string, any>, options: Record<string, any>): Promise<QueryResult>;
}

export type UpdateFaqBody = Partial<IFaq>;

export type NewCreatedFaq = Omit<IFaq, 'tags'>;