import mongoose from 'mongoose';
import toJSON from '../toJSON/toJSON';
import paginate from '../paginate/paginate';

import { IFaqDoc,IFaqModel } from './faq.interfaces';

const faqSchema = new mongoose.Schema<IFaqDoc, IFaqModel>(
  {
    question: {
      type: String,
      required: true,
      trim: true,
    },
    answer: [
      {
        answer: {
          type: String,
          required: true,
          trim: true,
        },
        tags: {
          type: [String],
          trim: true,
        },
        upvotes: {
          type: Number,
          trim: true,
        },
        downvotes: {
          type: Number,
          trim: true,
        },
        sentiment: {
          p_score: {
            type: Number,
            required: true,
            trim: true,
          },
          n_score: {
            type: Number,
            required: true,
            trim: true,
          },
          nu_score: {
            type: Number,
            required: true,
            trim: true,
          },
          comparative: {
            type: Number,
            trim: true,
          },
          tokens: {
            type: [String],
            trim: true,
          },
          words: {
            type: [String],
            trim: true,
          },
          positive: {
            type: [String],
            trim: true,
          },
          negative: {
            type: [String],
            trim: true,
          },
          neutral: {
            type: [String],
            trim: true,
          },
        },
        }
    ]

  },
  {
    timestamps: true,
  }
)

// add plugin that converts mongoose to json
faqSchema.plugin(toJSON);
faqSchema.plugin(paginate);

const Faq = mongoose.model<IFaqDoc, IFaqModel>('Faq', faqSchema);

export default Faq;