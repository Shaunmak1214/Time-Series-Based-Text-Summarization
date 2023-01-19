import httpStatus from 'http-status';
import { Request, Response } from 'express';
import catchAsync from '../utils/catchAsync';
import pick from '../utils/pick';
import { IOptions } from '../paginate/paginate';
import * as faqService from './faq.service';

export const createFaq = catchAsync(async (req: Request, res: Response) => {
  const faq = await faqService.createFaq(req.body);
  res.status(httpStatus.CREATED).send(faq);
});

export const getFaqs = catchAsync(async (req: Request, res: Response) => {
  const filter = pick(req.query, ['question', 'answer']);
  const options: IOptions = pick(req.query, ['sortBy', 'limit', 'page', 'projectBy']);
  const result = await faqService.queryFaqs(filter, options);
  res.send(result);
});
