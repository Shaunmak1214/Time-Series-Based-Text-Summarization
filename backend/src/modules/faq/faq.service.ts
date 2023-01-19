import httpStatus from 'http-status';
import Faq from './faq.model';
import ApiError from '../errors/ApiError';
import { IOptions, QueryResult } from '../paginate/paginate';
import { IFaqDoc, NewCreatedFaq } from './faq.interfaces';


export const createFaq = async (faqBody: NewCreatedFaq): Promise<IFaqDoc> => {
  const faq = Faq.create(faqBody);
  if(!faq) {
    throw new ApiError(httpStatus.BAD_REQUEST, 'Error creating FAQ');
  }
  return faq;
};

export const queryFaqs = async (filter: Record<string, any>, options: IOptions): Promise<QueryResult> => {
  const faqs = await Faq.paginate(filter, options);

  if(!faqs) {
    throw new ApiError(httpStatus.BAD_REQUEST, 'Error querying FAQs');
  }
  return faqs;
};