/*
 * Copyright (c) 2020 the original author or authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
import {Component, Input} from '@angular/core';

import {Application} from '../../data/interfaces/application';
import {ROUTERS_URL} from '../../data/enums/routers-url.enum';
import {BreadcrumbsFacade} from './breadcrumbs.facade';
import {Model} from '../../data/interfaces/model';

@Component({
  selector: 'app-breadcrumbs',
  templateUrl: './breadcrumbs.component.html',
  styleUrls: ['./breadcrumbs.component.scss']
})
export class BreadcrumbsComponent {
  ROUTERS_URL = ROUTERS_URL;
  maxNameLength = 30;
  @Input() model: Model;
  @Input() orgId: string;
  @Input() app: Application;

  constructor(private breadcrumbsFacade: BreadcrumbsFacade) {
  }
}
