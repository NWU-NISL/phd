// Copyright 2019-2020 the ProGraML authors.
//
// Contact Chris Cummins <chrisc.101@gmail.com>.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
#include "deeplearning/ml4pl/graphs/graphviz_converter.h"

#include <sstream>

#include "deeplearning/ml4pl/graphs/programl.pb.h"
#include "labm8/cpp/test.h"

namespace ml4pl {
namespace {

TEST(GraphVizConverter, EmptyGraph) {
  ProgramGraph graph;
  std::stringstream output;
  SerializeGraphVizToString(graph, &output);
  ASSERT_EQ(output.str(), "digraph main {\nsubgraph external {\n}\n}\n");
}

}  // namespace
}  // namespace ml4pl

TEST_MAIN();
